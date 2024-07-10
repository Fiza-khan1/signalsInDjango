from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_save,post_delete,post_init,pre_init,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print('_______________LOGIN-_________')
    print("SENDER:",sender)
    print("request:",request)
    print("user:",user.email)
    print(f'kwargs::{kwargs}')

@receiver(user_logged_out,sender=User)
def logOut_success(sender,request,user,**kwargs):

    print('____________________logout-_________')
    print("SENDER LOGOUT:",sender)
    print("request LOGOUT:",request)
    print("user:",user.email)
    print(f'kwargs::{kwargs}')


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("LOGIN FAILED")
    print("sender:",sender)
    print('Credentials:', credentials)
    print("Request:", request)

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("_____AT BEGINNING SAVE_____")
    print("sender:",sender)
    print('Instance:', instance)
    


@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
         print("__New record created___")
         print("sender:",sender)
         print('Instance:', instance)
         print("Created:",created)
    else:
         print(" record UPdated")
         print("sender:",sender)
         print('Instance:', instance)
         print("Created:",created)

@receiver(pre_delete,sender=User)
def at_pre_delete(sender,instance,**kwargs):
    print("__Pre delete__")
    print("SENDER:",sender)
    print('Instance:',instance)

@receiver(post_delete,sender=User)
def at_post_delete(sender,instance,**kwargs):
    print("POST DELETE")
    print("sender:",sender)
    print("Instance:",instance)

@receiver(pre_init,sender=User)
def at_pre_init(sender,*args,**kwargs):
    print("Pre init")
    print("sender:",sender)
    print(f'ARGS:{args}')
    print(f'kwargs:{kwargs}')

@receiver(post_init,sender=User)
def at_post_init(sender,*args,**kwargs):
    print("Pre init")
    print("sender:",sender)
    print(f'ARGS:{args}')
    print(f'kwargs:{kwargs}')


@receiver(request_started)
def at_request_start(sender, environ, **kwargs):
    print("Request started")
    print("Sender:", sender)
    print(f'Environ: {environ}')
    print(f'kwargs: {kwargs}')

@receiver(request_finished)
def at_request_end(sender, **kwargs):
    print("Request ended")
    print("Sender:", sender)
    print(f'kwargs: {kwargs}')

@receiver(got_request_exception)
def at_request_exception(sender,request, **kwargs):
    print("GOT exceptIOn")
    print("Sender:", sender)
    print("request:",request)
    print(f'kwargs: {kwargs}')

@receiver(pre_migrate)
def before_migrate(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
        print("Before migrate")
        print("Sender:", sender)
        print("verbosity:",verbosity)
        print(f'kwargs: {kwargs}')
        print('Interactive:',interactive)@receiver(pre_migrate)

@receiver(post_migrate)
def after_migrate(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
        print("After migrate")
        print("Sender:", sender)
        print("verbosity:",verbosity)
        print(f'kwargs: {kwargs}')
        print('Interactive:',interactive)

@receiver(connection_created)
def database_connection(sender,connection,**kwargs):
            print("DATABASE CONNECTION")
            print("Sender:", sender)
            print("connection:",connection)
            print(f'kwargs: {kwargs}')
     




    

 


    



