import streamlit as st
from calc.calc import Calc

st.title('Calculator')

chars = {
    'add': '+',
    'sub': '-',
    'mul': '*',
    'div': '/',
    'mod': '%'
}


def get_result(a, b, c):
    if c == 'add':
        return Calc(a, b).add()
    if c == 'sub':
        return Calc(a, b).sub()
    if c == 'mul':
        return Calc(a, b).mul()
    if c == 'div':
        return Calc(a, b).div()
    if c == 'mod':
        return Calc(a, b).mod()


with st.form('calc'):
    rolldown = st.selectbox(
        'Method',
        options=list(chars.keys())
    )
    first = st.number_input('First number', 0)
    second = st.number_input('Second number', 0)

    st.form_submit_button('Calculate')

st.write(
    f'{first} {chars.get(rolldown)} {second} =',
    str(get_result(first, second, rolldown))
)
