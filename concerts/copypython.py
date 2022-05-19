def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city_name']
            API_KEY = 'MyAppKey'
            url = 'https://api.yelp.com/v3/businesses/search'
            headers = {'Authorization': 'Bearer {}'.format(API_KEY)}
            params = {'term':'bar','location':city}
            req = requests.get(url, params=params, headers=headers)
            parsed = json.loads(req.text)
            businesses = parsed["businesses"]
            final_result = []

            for business in businesses:
                results = {
                'id': business['id'],
                'business': business['name'],
                'rating': business['rating'],
                'image_url': business['image_url']
                }
                final_result.append(results)

            context = {'final_result': final_result}
            return render(request, 'API/results.html', context)
    else:
        form = CityForm()
    return render(request, 'API/home.html', {'form':form})










def add_list(request,results):
    if request.method == 'POST':
        Bar = BarList(api_id=results,user=request.user)
        Bar.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'API/results.html')