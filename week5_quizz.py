##required_fuel = 25;
##actual_fuel = 5;
##
##print ('Question', actual_fuel < required_fuel);
##
##print(required_fuel > actual_fuel);
##print(actual_fuel <= required_fuel);
##print(actual_fuel >= required_fuel);
##print(required_fuel >= actual_fuel);
##print(required_fuel <= actual_fuel);

python = 1;
java = 2;
csharp = 3;
scheme = 4;
c = 1;
other = False;

##print("False");
#print(not (python == c));
##print((python == c) and (python == java));
##print((python < scheme) or (java > python));
##print(csharp >= scheme);
##print((python < scheme) and (java > python));
##print(((python == c) and (python == java)) or (c >= python));
##print((python == c) and (python != java) and (c >= python));
##print((python == c) or (python == java));
##print(scheme != java + python + c);
##print(other or (csharp == 3));
##print(python == c);
##print(python <= c);
##print(python != c);
##print((python == c) or (python != java) or (c >= python));		
##print(not (java <= python));

##results = [4, 3, 6]
##pass_grade = 4
##minimum = 7
##index = 0;
##
##if results[index] >= pass_grade and \
##   results[index] < minimum:
##    minimum = results[index]
##print('step 1');
##print(index);
##print(minimum);
##
##index = index + 1;
##print('step 2');
##print(index);
##print(minimum);
##
##if results[index] >= pass_grade and \
##   results[index] < minimum:
##    minimum = results[index]
##print('step 3');
##print(index);
##print(minimum);
##
##index = index + 1;
##print('step 5');
##print(index);
##print(minimum);
##
##if results[index] >= pass_grade and \
##   results[index] < minimum:
##    minimum = results[index]
##    
##print('step 6');
##print(index);
##print(minimum);

##def alarm_test(level, threshold) :
##    alarm = 3
##    if level >= threshold:
##        if level < 100:
##            alarm = 1;
##        alarm = 2
##        
##    return alarm;
##
##print(alarm_test(3, 4));
##print(alarm_test(5, 4));
##print(alarm_test(1, 2));
##print(alarm_test(4, 5));
##print(alarm_test(200, 99));
##print(alarm_test(400, 300));
##print(alarm_test(10, 10));
##print(alarm_test(200, 100));


