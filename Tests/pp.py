# from time import perf_counter
# from reader import readfile

# # kk = readfile('pp.json')
# # for i in kk:
# #     # print(kk)
# #     # print(kk[i])
# #     dk = kk[i]
# #     for k in kk[i]:
# #         v = kk[i]
# #         # print(v[k])

# # cmd = input(">> ").lower()
# # # print(kk[cmd])
# # if cmd in dk["command"]:
# #     print('yes', dk)
# # print(dk)

# # commands = readfile('pp.json')
# # for command_name in commands:
# # # command_name
# #     command_name = commands[command_name]
# # # command = content["command"]
# # # task = content["task"]
# # # task_type = content["task type"]
# # print("commands:", commands)
# # print("command name:", command_name)
# # # print("content:", content)
# # # print("command:", command)
# # # print("task:", task)
# # # print("task type:", task_type)

# # # cmd = input(">> ").lower()
# # # if

# # cmd = input(">> ").lower()
# # commands = readfile('pp.json')
# # for command_name in commands:
# #     # print(command_name)
# #     content = commands[command_name]
# #     command = content["command"]
# #     # print(command)
# #     if cmd in command:
# #         print(command)

# cmd = input(">> ")
# commands = readfile("pp.json")
# cmd = commands[cmd]
# task = cmd["task"]
# task_type = cmd["task type"]
# print(task)
# print(task_type)

# # command_file = readfile("pp2.json")
# # cmd  = input(">> ")
# # for content in command_file:
# #     print(content)
# #     command_names = command_file[content]
# #     command = command_names["command"]
# #     task = command_names["task"]
# #     task_type = command_names["task type"]

# #     if cmd in command:
# #         print('yes')
# #         if cmd in command_names:
# #             print('yes', command_names)

# import platform
# operating_system = platform.system()
# distribution = platform.release()
# if operating_system == "Linux":
#     if "arch" in distribution:
#         distribution = "Arch Linux"
#         print(distribution)

# import datetime
# hour = datetime.datetime.now().hour
# minute = datetime.datetime.now().minute
# second = datetime.datetime.now().second

# print(f"{hour}:{minute}:{second}")

# jf = "file.json"
# pf = "file.py"
# cf = ".file"
inp = input(">> ").lower()
if inp.endswith(".json"):
    print('yeah')
else:
    print('no')