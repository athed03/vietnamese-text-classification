# Depedencies
This project need to import sklearn library. pipeline on sklearn will be needed squential proses for vectorizing and classification. 
For preprocessing, this project need regex library to remove endline and number on paragraph. 

# Pretrained
this project use dataset that contain 10 topics of text, Văn hóa (Cultural),Pháp luật (Law), Chính trị Xã hội (Social Politics), Vì tình (Love), Khoa học (Science) ,Đời sống (Life),Sức khỏe(Health), Thể thao (Sport), Kinh doanh (Bussiness), Thế giới(World)

label	    text
The gioi	Đám cháy " lò thiêu " ở Philippines Trong ảnh...
Van hoa	    NSƯT Thanh Thanh Tâm thử thách với nghề đạo d...
Kinh doanh	Phòng Thương mại Hoa Kỳ (Amcham) vừa phối hợp ...
Vi tinh	    Có bao giờ bạn thắc mắc tại sao trong list của...
Kinh doanh	Theo TTXVN , hãng phim hoạt hình Walt Disne...

# How to run
biar sy aja isi yang ini


# Benchmark 
Total data train: ~50300

accuracy 0.871498620292617
                  precision    recall  f1-score   support

        The gioi       0.85      0.78      0.81      7567
        Suc khoe       0.66      0.67      0.66      2036
       Phap luat       0.68      0.78      0.72      2096
Chinh tri Xa hoi       0.84      0.90      0.87      5276
         Van hoa       0.79      0.92      0.85      3788
        Doi song       0.94      0.89      0.91      5417
      Kinh doanh       0.94      0.87      0.90      6716
         Vi tinh       0.99      0.94      0.97      6667
        Khoa hoc       0.84      0.95      0.89      6250
        The thao       0.95      0.85      0.90      4560

        accuracy                           0.87     50373
       macro avg       0.85      0.85      0.85     50373
    weighted avg       0.88      0.87      0.87     50373
# sample input output
sample test
=====
Những ngày qua, những người thường xuyên sử dụng các trang mạng xã hội đều biết đến một cô gái mới 20 tuổi đang tạo nên một sự chú ý cho mọi người khi liên tục đưa lên mạng những đoạn phim ngắn của chính mình trong bộ dạng rất khiêu gợi

In recent days, people who regularly use social networking sites know a 20-year-old girl is creating attention for people when constantly uploading her own short videos in the form of very erotic. 

result  Chính trị Xã hội