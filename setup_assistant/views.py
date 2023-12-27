from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import SetupForm

def setup_environment(request):
    if request.method == 'POST':
        form = SetupForm(request.POST)
        if form.is_valid():
            # Save the form data to environment variables or .env file
            # Redirect to the dashboard or a success page
            return redirect('dashboard')
    else:
        form = SetupForm()

    return render(request, 'setup_assistant/setup_form.html', {'form': form})