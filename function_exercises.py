def is_two(x):
    if x == 2:
        return True
    elif x == '2':
        return True
    else:
        return False
    
def is_vowel(x):
    if x.lower() in 'aeiouy':
        return True
    else: 
        return False
    
def is_vowel(x):
    if x.lower() in 'aeiouy':
        return False
    else: 
        return True


def cap_this(x):
    if x[0] not in 'aeiou':
        user_o = x.capitalize()
        return user_o
    else:
        return x
    
def tip_cal(tip_p, bill):
    if tip_p < 0.20:
        print('Your disrespect for working folk is palapable.')
        return round((tip_p/100) * bill, 2)
    elif tip_p >= 0.20:
        print('You have clearly been raised to respect those who work in the restaurant industry.')
        return round((tip_p/100)*bill, 2)
    
def discount_cal(item_price, discount_value):
    discount = (discount_value / 100) * item_price
    final_price = item_price - discount
    return (f'${round(final_price,2)}')


def handle_commas(input_no):
    no_comma_no = int(user_no.replace(',',''))
    return no_comma_no

def get_letter_grade(grade_in):
    if grade_in > 90:
        return 'A'
    elif grade_in > 80:
        return 'B'
    elif grade_in > 70:
        return 'C'
    elif grade_in > 60:
        return 'D'
    else:
        return 'F'
    
def remove_vowels(vowelfull):
    for letter in vowelfull:
        if letter in 'aeiouAEIOU':
            vowelfull = vowelfull.replace(letter, '')
    return vowelfull
    
    
def normalize_name(input_nom):
    not_ok = ('!','@','#','$','%','^','&','*','(',')',',')
    for char in input_nom:
        if char in not_ok:
            input_nom = input_nom.replace(char,'')
    input_nom = input_nom.strip()
    input_nom = input_nom.replace(' ','_')
    return input_nom.lower()
              
              
def cumlative_sum(user_nums):
    out_list = []
    sec_list = []
    for num in user_nums:
        sec_list.append(int(num))
        out_list.append(sum(sec_list))
    return out_list
    
    
