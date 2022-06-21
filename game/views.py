from django.shortcuts import render

# Create your views here.
class Check:
    def __int__(self):
        self.numbers = None

    def validation(self, numbers):
        try:
            number = [int(x) for x in numbers]
            if len(number) != 4:
                return 'Please, enter no more and no less than 4'
            if len(number) != len(set(number)):
                return 'Please, enter non-repeating numbers'
            for i in number:
                if i < 1 or i > 9:
                    return 'Please, enter a number from 1 to 10'
            self.numbers = number
        except ValueError:
            return 'Please, enter the number'

    def get_result(self):
        secret_nums = [5, 1, 2, 9]
        bulls = 0
        cows = 0
        for i in range(len(secret_nums)):
            if secret_nums[i] == self.numbers[i]:
                bulls += 1
            elif secret_nums[i] in self.numbers:
                cows += 1
        if bulls == 4:
            return f"You got it right!"
        elif bulls or cows:
            return f"You got {bulls} bulls, {cows} cows"
        else:
            return 'No identical numbers'
def game(request):
    check = Check()
    if request.method == 'GET':
        return render(request, 'main.html')
    else:
        numbers = request.POST.get('numbers').split()
        result = check.validation(numbers)
        if result:
            result
        else:
            result = check.get_result()
            result
        # result = get_result(numbers)
        context = {
            'numbers': request.POST.get('numbers'),
            'result': result
        }

        return render(request, 'main.html', context)
