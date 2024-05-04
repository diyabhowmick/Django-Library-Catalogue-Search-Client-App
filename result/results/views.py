from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        api_url = f'http://127.0.0.1:8000/book/{title}'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        book_data = response.json()
        if response.status_code == 200:
            book_data = response.json()
            return render(request, 'results.html', {'book_data': book_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch book results. Check Again!'})
    
        
    return render(request, 'index.html')



