# Korean_Semantic_Textual_Similarity
 Fine Tuning 'klue/roberta-large' with kor-sts, klue-sts-v1.1

 Best tuned version: 

 Training on klue-sts-v1.1 only (sts_v2.ckpt.3)

 pearsonr: 0.8817
 f1_score: 0.8353
 loss: 0.6619


 Training on both kor-sts and klue-sts-v1.1 (sts_vx.ckpt.3)

 Klue-STS 
 pearsonr: 0.8845,
 f1_score: 0.8502024291497976

 Kor-STS
 spearmanr: (correlation=0.835524139307486, pvalue=0.0),
 f1_score: 0.8382886149383612


 F1 Score: 
 Model trained on real-value (float), generated prediction converted into 0 and 1 (binary)
 with threshold of 3. 



 STS-API (tested and developed on a local setting)

 Included Files
 whole_vx3 (whole model saved), roberta_large_tok (klue/roberta-large tokenizer),
 sts_api.py, model_source.py

 Used Model
 sts_vx.ckpt.3 (fine tuned klue roberta large (mentioned above))

 Calls
 GET: returns predicted sts score between two sentences

 POST: returns predicted sts score between one sentence an multiple sentences




 References
 
 klue/roberta-large Model
 @misc{park2021klue,
  title={KLUE: Korean Language Understanding Evaluation},
  author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
  year={2021},
  eprint={2105.09680},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
  }

 kor-sts Dataset (sts-train.tsv, sts-dev.tsv, sts-test.tsv)
 @article{ham2020kornli,
  title={KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding},
  author={Ham, Jiyeon and Choe, Yo Joong and Park, Kyubyong and Choi, Ilji and Soh, Hyungjoon},
  journal={arXiv preprint arXiv:2004.03289},
  year={2020}
  }

 klue-sts-v1.1 Dataset (klue-sts-v1.1_train.json, klue-sts-v1.1_dev.json)
 @misc{park2021klue,
  title={KLUE: Korean Language Understanding Evaluation},
  author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
  year={2021},
  eprint={2105.09680},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
  }













