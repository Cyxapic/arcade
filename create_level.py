screen_size = 960, 800
 
w = screen_size[0] // 32
h = screen_size[1] // 32
size = 32


s = w-2

with open('resourses/levels/level_1.lvl', 'w') as fl:
    fl.writelines(f'{"*"*w}\n')
    for h1 in range(1, h-1):
        fl.writelines(f'*{" " * s}*\n')
    fl.writelines(f'{"*"*w}\n')
