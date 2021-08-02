import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect

        #1
        barcode_info = barcode.data.decode('utf-8')

        # frame, co-ordinates, bounding box color and rectangle thickness
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 3)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        # frame, barcode info, co-ordinates, font, text size, text color and text thickness
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 0.5 , (220, 20, 60), 1)

        #will create a .txt file in the directory
        with open("scanned_result.txt", mode ='w') as file:
            file.write("The scanned code is :- " + barcode_info)
    return frame

def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('QR/Barcode reader', frame)

        #escape key exit
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()

# Running the main function
if __name__ == '__main__':
    main()