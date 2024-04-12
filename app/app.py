import streamlit as st
from calc.calc import Calc

st.title('Calculator')

chars = {
    'add': '+',
    'sub': '-',
    'mul': '*'
}


def get_result(a, b, c):
    if c == 'add':
        return Calc(a, b).add()
    if c == 'sub':
        return Calc(a, b).sub()
    if c == 'mul':
        return Calc(a, b).mul()


with st.form('calc', border=False):
    rolldown = st.selectbox('Method', options=['add', 'sub', 'mul'])
    first = st.number_input('Firs number', 0)
    second = st.number_input('Second number', 0)

    st.form_submit_button('Calculate')

st.write(
    f'{first} {chars.get(rolldown)} {second} =',
    str(get_result(first, second, rolldown))
)
