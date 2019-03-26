
import cv2
import numpy as np


def func(inputf, output, threshold1, threshold2, fr,kernel_size,blur, color_hard, color_soft):
    '''change path to input file path'''
    color_hard=np.array(color_hard, dtype='int')
    color_soft=np.array(color_soft, dtype= 'int')
    vid = cv2.VideoCapture(inputf)
    fourcc = cv2.VideoWriter_fourcc(*'X264')

    '''change output.mp4 to any output file name and 24.0 to output framerate needed'''
    
    x_len=int(vid.get(3))
    y_len=int(vid.get(4))
    out = cv2.VideoWriter(output, 0x31637661, fr,( x_len , y_len ))

    ret, frame = vid.read()
    

    while (True):
        ret, frame = vid.read()
        if ret == True:

            '''play with 150 and 200(increase/decrease to get desired edge output'''
            
            frame = cv2.Canny(frame, threshold1, threshold2)
            frame =np.asarray(frame)
            frame =np.expand_dims(frame, axis=2)
            
#            cv2.imshow("gh1", frame)            
            kernel = np.ones((kernel_size, kernel_size), np.float32)
            # frame=cv2.filter2D(frame,-1,kernel)

            frame2 = cv2.dilate(frame, kernel, 1)
            #print(frame2)
#            frame2 = 
            #frame2 = (frame2*(1/255)) #*color_soft
            
            frame2 = cv2.blur(frame2, (blur,blur))
            
#            frame=np.array( (frame//255)*color_hard, dtype='int')
#            cv2.imshow("gh2", frame2)
            frame2=cv2.add(frame,frame2)
#            frame2=frame+frame2
            cv2.imshow("gh3", frame2)
            
            out.write(frame2)

            '''press q to stop process'''

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    vid.release()
    out.release()
    # cv2.waitKey(0)
    ##
    # vid= cv2.VideoCapture("F:\\premiere export\\output.mp4")
    # while(True):
    #    ret,frame=vid.read()
    #    if ret==True:
    #        cv2.imshow("gh2",frame)
    #
    #        out.write(frame)
    #        if cv2.waitKey(1) & 0xFF==ord('q'):
    #            break
    #    else:
    #        break

    cv2.destroyAllWindows()



#inputf = input("Enter name/path of input file: ")
#outputf = input("Enter name/path of output file: ")
#th1 = int(input("Enter threshold 1: "))
#th2 = int(input("Enter threshold 2: "))
#fr = int(input("Enter framerate: "))
#kernel_size=int(input("Enter kernel size(3 for less glow/thickness, higher for glowey/thick edges): "))
#blur=int(input("Enter blur size(5 to something): "))
#color_hard=(input("Enter color of hard line (bgr format, hex, no spaces eg 04cfa1): "))
#color_soft=(input("Enter color of hard line (bgr format, hex, no spaces eg 04cfa1): "))
#color_hard=[int('0x'+color_hard[0:2],16), int('0x'+color_hard[2:4],16),  int('0x'+color_hard[4:],16) ]
#color_soft=[int('0x'+color_soft[0:2],16), int('0x'+color_soft[2:4],16),  int('0x'+color_soft[4:],16) ]

#func(inputf, outputf, th1, th2, fr / 1,kernel_size,blur, color_hard, color_soft)

func("concert_2.mp4","op.mp4",100,100,24,5,10, [0, 100, 200],[200, 100, 0])


