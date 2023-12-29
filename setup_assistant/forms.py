from django import forms

class SetupForm(forms.Form):
    # Docker Swarm Initialization
    master_node_ip = forms.CharField(label='Master Node IP', max_length=15)
    worker_node_token = forms.CharField(label='Worker Node Token', max_length=100)
    # Service Deployment
    service_name_yml = forms.CharField(label='Service Name YML', max_length=100)
    # Dashboard Configuration
    dashboard_env_vars = forms.CharField(label='Dashboard Environment Variables', max_length=500)
    # Monitoring Tools Setup
    monitoring_prometheus_url = forms.CharField(label='Prometheus URL', max_length=100)
    monitoring_grafana_url = forms.CharField(label='Grafana URL', max_length=100)
    # PiHole Deployment
    pihole_timezone = forms.CharField(label='PiHole Timezone', max_length=50)
    pihole_admin_password = forms.CharField(label='PiHole Admin Password', max_length=100, widget=forms.PasswordInput)
    # Alerting and Notifications
    alerting_rules = forms.CharField(label='Alerting Rules', max_length=500)
    # SSL Configuration
    ssl_certificate = forms.CharField(label='SSL Certificate', max_length=1000)
    ssl_certificate_key = forms.CharField(label='SSL Certificate Key', max_length=1000)
    # Final Steps Verification
    final_steps_verification = forms.CharField(label='Final Steps Verification', max_length=500)