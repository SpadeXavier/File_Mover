import os 
import shutil 

def move_files(source, target, date, center, group, teacher):
    lessons = "LessonPlans" 
    videos = "Videos" 
    teacher_abbr = teacher.split('_')[0][0] + teacher.split('_')[1][0] 
    print(teacher_abbr) 
    
    source_path = source + "/" 
    target_path = target + "/" 
    date_path = target_path + date + "/" 
    center_path = date_path + center + "/" 
    group_path = center_path + group + "/" 
    teacher_path = group_path + teacher + "/" 
    lessons_path  = teacher_path + lessons + "/" 
    videos_path = teacher_path + videos + "/" 
    to_create_paths = [date_path, center_path, group_path,
            teacher_path, lessons_path, videos_path] 

    # -- create necessary directory structure 
    for p in to_create_paths:
        if not os.path.exists(p):
            os.makedirs(p) 
    files = os.listdir(source_path)

    img_counter = 1 
    mov_counter = 1
    for f in files:
        final_path = ''
        if 'mov' in f:
            new_f = "{}_{}_{}_{}_{}V.mov".format(date, center, group, 
                    teacher_abbr, mov_counter)
            final_path = videos_path 
            mov_counter += 1
        elif 'img' in f:
            new_f = "{}_{}_{}_{}_{}LP.img".format(date, center, group, 
                    teacher_abbr, img_counter)
            final_path = lessons_path 
            img_counter += 1

        shutil.copy(source_path+f, final_path)
        shutil.move(final_path+f, final_path+new_f) 

def check_input(date, center, group, teacher):
    if '2017' not in date:
        raise ValueError("Make sure correct year is in date") 
    if len(center) > 5:
        raise ValueError("Please abbreviate the center's name")
     
def get_input():
    date = input("Enter the month+year: ") 
    center = input("Enter the center abbreviated: ") 
    group = input("Enter the group: ") 
    teacher = input("Enter the teacher: ") 
    teacher = '_'.join(teacher.split(' '))  
    return (date, center, group, teacher) 

source = "DCIM"
target = "Hard_Drive" 
# date = "Oct2017" 
# center = "MLK" 
# group = "Toddler1Family1" 
# teacher = "Carol_Fullwood" 
date, center, group, teacher = get_input()
move_files(source, target, date, center, group, teacher) 









