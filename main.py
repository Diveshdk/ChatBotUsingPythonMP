import openai

print("Welcome to ChatGPT API")
my_secret = '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'

openai.api_key = my_secret


def main():
  chat_completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role":
          "user",
          "content":
          "Here is syllabus of Engineering Mathematics/maths 3, There are 6 modules in semester 3 as follows: 1.Laplace Transform , 2.Inverse Laplace Transform ,3.Fourier Series: ,4.Complex Variables: ,5.Statistical Techniques ,6.Probability . Important books for maths are 1 	Higher Engineering Mathematics, Dr. B. S. Grewal, Khanna Publication. 2 	Advanced Engineering Mathematics, Erwin Kreyszig, Wiley Eastern Limited. 3 	Advanced Engineering Mathematics, R. K. Jain and S. R. K. Iyengar, Narosa Publication. 4 	Complex Variables and Applications, Brown and Churchill, McGraw-Hill Education.  5 	Probability, Statistics and Random Processes, T. Veerarajan, McGraw-Hill Education. 6 	Theory and Problems of Fourier Analysis with applications to BVP, Murray Spiegel, Schaum’s Outline Series."
      }, {
          "role": "user",
          "content": "what book should I refer for maths?"
      }])

  print(chat_completion.choices[0].message['content'])


if __name__ == "__main__":
  main()
