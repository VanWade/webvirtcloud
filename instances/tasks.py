# Create your tasks here
from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from celery.task.base import PeriodicTask
# import datetime
from celery import task
from webvirtcloud import celery_app
from computes.models import Compute
from vrtManager.hostdetails import wvmHostDetails
from vrtManager.instance import wvmInstance, wvmInstances
from vrtManager.connection import connection_manager
from vrtManager.util import randomPasswd
from .models import VM
from celery.utils.log import get_task_logger
from libvirt import libvirtError
import os
from django.core.cache import caches

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webvirtcloud.settings')

logger = get_task_logger(__name__)


# @PeriodicTask(run_every=datetime.timedelta(seconds=3))
# def test_print():
#     print('hello celery')

# @app.tasks(name='test_print')
# def test_print():
#     print('hello celery')
@task()
def test_print():
    print('hello celery')


@celery_app.task()
def test_logger():
    logger = get_task_logger(__name__)
    logger.info('hello celery')


@celery_app.task()
def update_kvm_status():
    computes = Compute.objects.all()
    all_vms = []
    for comp in computes:
        if connection_manager.host_is_up(comp.type, comp.hostname):
            try:
                conn = wvmHostDetails(comp, comp.login, comp.password, comp.type)
                for vm_name, vm_info in conn.get_host_instances().items():
                    vm = list()
                    vm_object, created = VM.objects.update_or_create(compute_id=comp.id,
                                                                     name=vm_name,
                                                                     defaults={'status': vm_info['status'],
                                                                               'vcpu': vm_info['vcpu'],
                                                                               'memory': vm_info['memory'],
                                                                               'description': vm_info['description'],
                                                                               'title': vm_info['title'],
                                                                               'uuid': vm_info['uuid']})
                    if created:
                        logger.info('vm {} was created'.format(vm_name))
                    else:
                        logger.info('vm {} was updated'.format(vm_name))
                    vm.extend([vm_name, comp.name, vm_info["status"], vm_info["vcpu"], vm_info["memory"], comp.id,
                               vm_info['uuid']])
                    all_vms.append(vm)
            except Exception as e:
                logger.error(e)
                conn.close()
    logger.info('Caching all_vms:{}'.format(all_vms))
    caches['default'].set('all_vms', all_vms, None)
