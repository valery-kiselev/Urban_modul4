def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
        return
    inner_function()
    return

test_function()
#inner_function()    # ошибка: NameError: name 'inner_function' is not defined.
                    # NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?


