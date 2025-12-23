def squere_numbers(numbers):
    result = []
    for n in numbers:
        result.append(n*n)
    return result

print(squere_numbers([1,2,3,4]))

studants=[{"name":"shubhangi","age":33},
          {"name":"gaurav","age":35}
          ]

for studant in studants:
    print (studant["name"], studant["age"])