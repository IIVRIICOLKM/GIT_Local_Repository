import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

def generate_pass(length, array, password, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)
    return password

def regenerate_password():
    while True:
        # 패스워드 길이 입력
        pass_len = int(input("Enter Password Length: "))
        
        # 50-30-20 비율로 길이 설정
        alpha_len = pass_len // 2
        num_len = math.ceil(pass_len * 30 / 100)
        special_len = pass_len - (alpha_len + num_len)

        password = []
        
        # 알파벳, 숫자, 특수문자 비율에 맞게 패스워드 생성
        password = generate_pass(alpha_len, alpha, password, True)
        password = generate_pass(num_len, num, password)
        password = generate_pass(special_len, special, password)
        
        # 생성된 패스워드 셔플
        random.shuffle(password)

        # 리스트를 문자열로 변환
        gen_password = ''.join(password)

        # 생성된 패스워드 출력
        print(f"Generated Password: {gen_password}")

        # 재생성 여부 묻기
        if input("Do you want to regenerate? (y/n): ").lower() == 'n':
            break

# check password strength
def check_password_strength(password):
    strength = 0
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c in special for c in password):
        strength += 1
    return strength



# execute regenerate_password 
regenerate_password()
