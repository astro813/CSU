from django.shortcuts import render


def index(request, *args, **kwargs):
    print(request)
    if(args):
        print(args[0])
        return render(request, 'index.html', {'user_id': args[0]})
    else:
        return render(request, 'index.html')
