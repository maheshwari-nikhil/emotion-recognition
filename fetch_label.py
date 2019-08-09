class FetchLabel():

    def get_emotion(self, file_path):
        item = file_path.split('/')[-1]
        if item[6:-16]=='02' and int(item[18:-4])%2==0:
            return 'female_calm'
        elif item[6:-16]=='02' and int(item[18:-4])%2==1:
            return 'male_calm'
        elif item[6:-16]=='03' and int(item[18:-4])%2==0:
            return 'female_happy'
        elif item[6:-16]=='03' and int(item[18:-4])%2==1:
            return 'male_happy'
        elif item[6:-16]=='04' and int(item[18:-4])%2==0:
            return 'female_sad'
        elif item[6:-16]=='04' and int(item[18:-4])%2==1:
            return 'male_sad'
        elif item[6:-16]=='05' and int(item[18:-4])%2==0:
            return 'female_angry'
        elif item[6:-16]=='05' and int(item[18:-4])%2==1:
            return 'male_angry'
        elif item[6:-16]=='06' and int(item[18:-4])%2==0:
            return 'female_fearful'
        elif item[6:-16]=='06' and int(item[18:-4])%2==1:
            return 'male_fearful'
        elif item[6:-16]=='01' and int(item[18:-4])%2==0:
            return 'female_neutral'
        elif item[6:-16]=='01' and int(item[18:-4])%2==1:
            return 'male_neutral'
        elif item[6:-16]=='07' and int(item[18:-4])%2==0:
            return 'female_disgusted'
        elif item[6:-16]=='07' and int(item[18:-4])%2==1:
            return 'male_disgusted'
        elif item[6:-16]=='08' and int(item[18:-4])%2==0:
            return 'female_surprised'
        elif item[6:-16]=='08' and int(item[18:-4])%2==1:
            return 'male_surprised'
        elif item[:1]=='a':
            return 'male_angry'
        elif item[:1]=='f':
            return 'male_fearful'
        elif item[:1]=='h':
            return 'male_happy'
        elif item[:1]=='n':
            return 'male_neutral'
        elif item[:2]=='sa':
            return 'male_sad'
        elif item[:1]=='d':
            return 'male_disgusted'
        elif item[:2]=='su':
            return 'male_surprised'
        
