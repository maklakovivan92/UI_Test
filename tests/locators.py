# Кнопка "Войти в аккаунт" на главной странице
LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"

# Кнопка "Личный кабинет" в шапке страницы
PROFILE_BUTTON = "//a[@href='/account']"

# Поле Email на экране авторизации
EMAIL_INPUT = "//div[.//label[text()='Email']]//input"

# Поле Пароль на экране авторизации
PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input"

# Кнопка "Войти" на форме авторизации
SUBMIT_LOGIN_BUTTON = "//button[text()='Войти']"

# Кнопка "Зарегистрироваться" на форме авторизации
REGISTER_LINK = "//a[text()='Зарегистрироваться']"

# Кнопка "Восстановить пароль" на форме авторизации
FORGOT_PASSWORD_LINK = "//a[text()='Восстановить пароль']"

# Поле "Имя" на странице регистрации
REGISTER_NAME_INPUT = "//label[text()='Имя']/following-sibling::input"

# Поле Email на странице регистрации
REGISTER_EMAIL_INPUT = "//label[text()='Email']/following-sibling::input"

# Поле Пароль на странице регистрации
REGISTER_PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input"

# Кнопка "Зарегистрироваться" на странице регистрации
REGISTER_SUBMIT_BUTTON = "//button[text()='Зарегистрироваться']"

# Ошибка "Некорректный пароль" на странице регистрации
PASSWORD_ERROR = "//p[contains(text(),'Некорректный пароль')]"

# Кнопка "Войти" на странице регистрации 
LOGIN_FROM_REGISTER_LINK = "//a[@href='/login' and text()='Войти']"

# Кнопка "Войти" на странице регистрации
LOGIN_FROM_FORGOT_PASSWORD_LINK = "//a[@href='/login' and text()='Войти']"

# Кнопка "Войти" на странице восстановления пароля
FORGOT_PASSWORD_SUBMIT_BUTTON = "//button[text()='Восстановить']"

# Кнопка "Оформить заказ" в авторизованном аккаунте
MAKE_ORDER_BUTTON = "//button[text()='Оформить заказ']"

# Кнопка "Личный кабинет" в авторизованном аккаунте
PROFILE_BUTTON_AUTH = "//a[@href='/account']"

# логотип "Stellar Burgers" в авторизованном аккаунте
LOGO_BUTTON = "//a[@href='/']"

# Кнопка "Сохранить" в личном кабинете
SAVE_PROFILE_BUTTON = "//button[text()='Сохранить']"

# Кнопка "Конструктор" в авторизованном аккаунте
CONSTRUCTOR_BUTTON = "//p[text()='Конструктор']"

# Кнопка "Выход" в авторизованном аккаунте
LOGOUT_BUTTON = "//button[text()='Выход']"

# Кнопка "Булки"
BUNS_TAB = "//div[contains(@class,'tab_tab__')][.//span[text()='Булки']]"

# Кнопка "Соусы"
SAUCES_TAB = "//div[contains(@class,'tab_tab__')][.//span[text()='Соусы']]"

# Кнопка "Начинки"
FILLINGS_TAB = "//div[contains(@class,'tab_tab__')][.//span[text()='Начинки']]"
