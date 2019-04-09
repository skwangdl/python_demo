import os
import time

# demo about run command in enviroment using python
def backup():
    source = ['"D:\\temp\\temp_source"']
    target_dir = 'D:\\temp\\temp_target'
    target = target_dir + os.sep + \
             time.strftime('%Y%m%d%H%M%S') + '.zip'
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
    print('Zip command is:')
    print(zip_command)
    print('Running:')
    zip_command = 'dir'
    if os.system(zip_command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup failed')

if __name__ == '__main__':
    backup()