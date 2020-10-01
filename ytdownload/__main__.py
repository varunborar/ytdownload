import youtube_dl 
import sys

def main():
    print('in main')
    args = sys.argv[1]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))

    ydl_opts = {} 
  
    def dwl_vid(): 
        with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
            ydl.download([zxt]) 
    link_of_the_video = args
    zxt = link_of_the_video.strip() 
  
    dwl_vid() 

if __name__ == '__main__':
    main()
  

  

    
    