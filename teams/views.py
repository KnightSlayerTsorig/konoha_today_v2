from django.shortcuts import render


def teams(request):
    return render(request, 'teams/teams.html')


def team_5(request):
    return render(request, 'teams/team_5.html')


def team_7(request):
    return render(request, 'teams/team_7.html')


def team_10(request):
    return render(request, 'teams/team_10.html')


def team_15(request):
    return render(request, 'teams/team_15.html')
