weather = input("Tell me the wheather eg. Sunny ,Rainy ,Hot ,Snowy etc,so that AI suggests you an activity :").strip().lower()

if weather== 'sunny':
    print("AI Recommends you to Go for a walk")
elif weather== 'rainy':
    print(" AI recommends: Maybe take a shower — you might be stinking")
elif weather== 'hot': 
    print("AI Recommends you to Read a book in ac if there is")
elif  weather== 'snowy':
    print("AI Recommends you to make a snowman")
else:
    print("There is no imformation about "+weather+" provide in this AI model ") 