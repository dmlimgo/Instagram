# Instagram로 CSS연습하기

> Django의 CRUD 강의를 따라한 Instagram 앱에 실제 Instagram의 HTML구조와 CSS를 따라해 보았습니다.





## Install

python 가상환경에서 진행

```bash
$ pip install -r requirements.txt
```

```bash
$ python manage.py runserver
```





## 로그인 페이지

인스타그램 웹 페이지의 소스코드를 참조하여 **레이아웃**을 어떻게 구성하는지 배울 수 있었습니다.

CSS의 Display의 block과 flex를 주로 사용하면서 **레이아웃**을 구성하는 방법을 익힐 수 있었고, padding과 margin을 어떻게 구분하여 사용하는지 배울 수 있었습니다.

가장 어려웠던 것은 **ModelForm**으로 구성된 로그인Form과 회원가입Form에 **CSS**를 적용하는 것 이었습니다.

자세한 내용은 하단에 있습니다.

<img src="images\insta2.PNG" alt="insta2" style="zoom: 50%;" />

<img src="images\insta1.PNG" alt="insta1" style="zoom:50%;" />

ModelForm을 이용하여 Form을 구성하면 label과 placeholder값을 html에서는 수정해주기 힘듭니다(password의 경우). 

이를 아래와 같이 Form을 생성하는 단계(init을 선언해 초기화하는 단계)에서 super를 이용해 class를 적용시킨 상태로 생성할 수 있습니다.

그럼 위의 로그인화면과 같이 ModelForm에서도 각각 class를 적용해 줄 수 있습니다.

```python
# forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Profile

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserCustomCreationForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label=''
            field.help_text=''
        self.fields['email'].widget.attrs.update({'placeholder': '이메일 주소', 'class': 'input-box'})
        self.fields['username'].widget.attrs.update({'placeholder': '사용자 이름', 'class': 'input-box'})
        self.fields['password1'].widget.attrs.update({'placeholder': '비밀번호', 'class': 'input-box'})
        self.fields['password2'].widget.attrs.update({'placeholder': '비밀번호 확인', 'class': 'input-box'})
```

