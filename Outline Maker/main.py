import cv2
from rembg import remove

def main (image_path, output_name):
    image = cv2.imread(image_path)
    #resizing it for a better view due to my 14 inch screen
    image = cv2.resize(image,[1200,700]) 
    cv2.imshow( "Input Image",image)
    cv2.waitKey(0)
    
    
    while True:
        img = image.copy()
        r = cv2.selectROI("select the area (Press 'Enter' to continue and 'c' to stop)", image)

        # Crop image
        cropped_image = img[int(r[1]):int(r[1]+r[3]),
                            int(r[0]):int(r[0]+r[2])]
        cropped_wo_bg = remove( cropped_image)
        gray= cv2.cvtColor(cropped_wo_bg, cv2.COLOR_BGR2GRAY)

        edges= cv2.Canny(gray,30,200)

        contours, hierarchy= cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img[int(r[1]):int(r[1]+r[3]),
            int(r[0]):int(r[0]+r[2])], contours, -1, (0,255,0),2, hierarchy= hierarchy)
        
        cv2.imwrite("Results/" + output_name, img)
        cv2.imshow('Output Image',img)
        cv2.waitKey(1)
        if  0xFF == ord('q'):
            break
main(r'Images\2.jpg', "2.jpg")