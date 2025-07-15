import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def add_video(videos):
    name=input("Enter the video name")
    time=input("Enter the video duration")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos,start=1): # change the values into indexed tupples
        print(f"{index}.{video['name']}, Duration:{video['time']}")
    print("\n")
    print("*"*70)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to update"))
    if 1 <= index <= len(videos):
        name=input("Enter the video name")
        time=input("Enter the video duration")
        videos[index-1]={"name":name,"time":time}
        save_data_helper(videos)
    else:
        print("Invalid index number")

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number you want to update"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index number")
    



def main():
    videos = load_data()
    while True:
        print("----Youtube Manager----| Enter your choice")
        print("1.Add a youtube video")
        print("2.List all videos")
        print("3.Update a youtube video")
        print("4.Delete a youtube video")
        print("5.Exit the application")

        choice=input("Enter your choice: ")

        match choice:
            case '1':
                add_video(videos)
            case '2':
                list_all_videos(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Please enter a valid choice")

if __name__ == "__main__": # dunder
    main()
    


