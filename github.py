print("****welcome to my to-do app****")

user_list = []
while True:
  user_option = int(input('choose an option below: \n' '1. Add\n' '2. View\n' '3. Edit\n' '4. Delete\n' '5. Exit\n' '6. Clear\n'))
  if user_option == 1:
       #   add a task
   add_input = input("Enter to-do: \n")
   user_list.append(add_input)
   print(f"{add_input} has been added to your to-do successfully")
   #while loop(infinity loop)
  elif user_option == 2:
       # viewing added task
        if not user_list:
               print('todo list is empty')
               # for add-input in user_list:
        else:
               print('to do list')
               for index,item in enumerate(user_list, start=1):
                      print(f'{index}.item')
  elif user_option == 3:
       # editing a task
       if not user_list:
        print('there is no items to edit')
       else:
            try:
                     task_number = int(input('enter task number you eant to edit \n'))
                     new_task = input('enter new task item')
                     print(f'{add_input} is successfully edited')
            except(ValueError, IndexError):
                   print('invalid task item')
  elif user_option == 4:
        if not user_list:
               print('unavialable')
        else:
            try:
                   task_number = int(input('Enter task number you want to delete!\n'))
                   user_list.pop(task_number -1)
                   print(f"{add_input} is successfully deleted")
            except(ValueError, IndexError):
                   print('Invalid task number')
  elif user_option == 5:
        print('Good Bye')
  else:
        print('error')      
  if user_option == 6:
       # clearing all task
   user_list.clear()
  print('list has been cleared')
else:
              print('unchange')
              
