def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg): #start = 시작 // end = 목표 // other = 나머지
    # 코드를 입력하세요.
    if num_disks == 0:
        return(num_disks, start_peg, end_peg)
    
    other_peg = 6 - start_peg - end_peg
 
    hanoi(num_disks - 1, start_peg, other_peg)

    move_disk(num_disks, start_peg, end_peg)

    hanoi(num_disks - 1, other_peg, end_peg)
    
    
     

         
#hanoi(1, 1, 3)
#hanoi(2, 1, 3)
hanoi(3, 1, 3)

#원판이 3개 일 때.. 
'''
start_peg other_peg end_peg
  1           2        3

 

'''
#start_peg + end_peg + other_peg = 1번 2번 3번 기둥

