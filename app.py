import sys
try:
    import cgi
except ImportError:
    try:
        import legacy_cgi as cgi
        sys.modules['cgi'] = cgi
    except ImportError:
        pass

from mylevin.wsgi import application as app

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylevin.settings')
    execute_from_command_line(sys.argv)
