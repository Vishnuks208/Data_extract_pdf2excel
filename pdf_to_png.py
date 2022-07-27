from pdf2image import convert_from_path

image = convert_from_path('test.pdf')

for i in range(len(image)):
    image[i].save('Invoice'+str(i+1)+'.png','PNG')
