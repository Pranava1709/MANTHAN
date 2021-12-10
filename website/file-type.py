# import filetype
#
#
# def main():
#     kind = filetype.guess('static/images/bg.jpg')
#     if kind is None:
#         print('Cannot guess file type!')
#         return
#
#     print('File extension: %s' % kind.extension)
#     print('File MIME type: %s' % kind.mime)
#
#
# if __name__ == '__main__':
#     main()
import os
for f in os.listdir("C:\\Users\\gbans\\Desktop\\final\\website\\website\\uploaded_image"):
    print(f)
