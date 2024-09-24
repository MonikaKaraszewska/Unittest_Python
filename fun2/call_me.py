def call_me(name='zfunkcji'):
    print(f"hello {name}")
    print('module name', __name__)

def nie_call():
    print('nie dzwon do mnie')

if __name__ == '__main__':
    call_me('call z if')

call_me('mk')
nie_call()
