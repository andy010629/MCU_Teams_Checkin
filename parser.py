from bs4 import BeautifulSoup



def get_absent_student():

  all_student = set()
  check_student = set()
  title = ""

  # check_student.add('07190226')
  
  f = open('check_student.txt', encoding='utf-8')
  soup = BeautifulSoup(f.read(), 'lxml')
  title = soup.select('.thread-subject.padded-content')[0].text
  soup = soup.select(
      '.conversation-common.conversation-reply.conversation-not-collapsed')
  for ele in soup:
      split_text = ele.text.split('的回覆')[0]
      stu_id = ''.join(char for char in split_text if char.isdecimal())
      stu_name = ''.join(
          char for char in split_text if not char.isdecimal()).split('來自')[1]
      check_student.add(stu_id)

  f = open('course_student.txt', encoding='utf-8')
  soup = BeautifulSoup(f.read(), 'lxml')
  course_student = soup.select('#ContentPlaceHolder1_ChkLStno > tr > td')
  for stu in course_student:
      stu_id = stu.input.attrs['value']
      stu_name = ''.join([text for text in stu.text if not text.isdecimal()])
      all_student.add(stu_id)

  print(title)
  print(f'出席人數: {len(check_student)}/{len(all_student)}')
  print('未出席:', [*(all_student - check_student)])


  print("\n*** Copy the following code to web console ***")
  print(f"let uncheck = {[*all_student - check_student]}")
  print("""for(let i=0;i<uncheck.length;i++){
      $('input[value="'+uncheck[i]+'"]').click()
  }
  """)
