from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kwiz_question1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Завжди, я ж не хочу сваритися!", callback_data="answer1_1")],
    [InlineKeyboardButton(text="Ну, тільки якщо це реально має сенс.", callback_data="answer1_2")],
    [InlineKeyboardButton(text="Рідко, моя думка — це святе.", callback_data="answer1_3")],
    [InlineKeyboardButton(text="Ніколи! Я тут для того, щоб бути собою.", callback_data="answer1_4")]
])

kwiz_question2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Лише інколи, я ж янгол у душі.", callback_data="answer2_1")],
    [InlineKeyboardButton(text="Ну, буває, але тільки коли треба.", callback_data="answer2_2")],
    [InlineKeyboardButton(text="Чесно? Досить часто.", callback_data="answer2_3")],
    [InlineKeyboardButton(text="Ніколи! Я як відкрита книга.", callback_data="answer2_4")]
])

kwiz_question3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вогонь — це чистий адреналін!", callback_data="answer3_1")],
    [InlineKeyboardButton(text="Вода — я люблю спокій і потік.", callback_data="answer3_2")],
    [InlineKeyboardButton(text="Земля — я про стабільність і силу.", callback_data="answer3_3")],
    [InlineKeyboardButton(text="Повітря — свобода та легкість, моє все.", callback_data="answer3_4")]
])

kwiz_question4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Я створений для великих справ!", callback_data="answer4_1")],
    [InlineKeyboardButton(text="Допомагати іншим — це мій vibe.", callback_data="answer4_2")],
    [InlineKeyboardButton(text="Спокій і мир — головне.", callback_data="answer4_3")],
    [InlineKeyboardButton(text="Я за fun і авантюри на максимум.", callback_data="answer4_4")]
])

kwiz_question5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бути успішним, як топ-блогер.", callback_data="answer5_1")],
    [InlineKeyboardButton(text="Любов і тусовка з близькими.", callback_data="answer5_2")],
    [InlineKeyboardButton(text="Внутрішній дзен і Netflix вечорами.", callback_data="answer5_3")],
    [InlineKeyboardButton(text="Творити і ловити кайф.", callback_data="answer5_4")]
])

kwiz_question6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Цілеспрямованість, драйв, сила.", callback_data="answer6_1")],
    [InlineKeyboardButton(text="Емпатія, турбота, тепло.", callback_data="answer6_2")],
    [InlineKeyboardButton(text="Баланс, гармонія, спокій.", callback_data="answer6_3")],
    [InlineKeyboardButton(text="Вогонь, хаос, рух.", callback_data="answer6_4")]
])

kwiz_question7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Червоний — бо я на піку.", callback_data="answer7_1")],
    [InlineKeyboardButton(text="Синій — chill mode on.", callback_data="answer7_2")],
    [InlineKeyboardButton(text="Зелений — природа, мир, релакс.", callback_data="answer7_3")],
    [InlineKeyboardButton(text="Жовтий — бо я ходяча радість!", callback_data="answer7_4")]
])

kwiz_question8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Як challenge, який я виграю.", callback_data="answer8_1")],
    [InlineKeyboardButton(text="Як подарунок, треба юзати!", callback_data="answer8_2")],
    [InlineKeyboardButton(text="Як шлях до себе — я в пошуку.", callback_data="answer8_3")],
    [InlineKeyboardButton(text="Як гру, у якій я головний герой.", callback_data="answer8_4")]
])

kwiz_question9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Бути босом у своїй справі.", callback_data="answer9_1")],
    [InlineKeyboardButton(text="Родина і друзі — це святе.", callback_data="answer9_2")],
    [InlineKeyboardButton(text="Внутрішній спокій і зелений чай.", callback_data="answer9_3")],
    [InlineKeyboardButton(text="Нові знання і прокачка себе.", callback_data="answer9_4")]
])

kwiz_question10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="У мене є все, що треба.", callback_data="answer10_1")],
    [InlineKeyboardButton(text="Я працюю над своїм 'світовим туром'.", callback_data="answer10_2")],
    [InlineKeyboardButton(text="Гроші? Meh, це не головне.", callback_data="answer10_3")],
    [InlineKeyboardButton(text="Я вже бачу себе у Bugatti.", callback_data="answer10_4")]
])

finall = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="НАЖИМАЙ!", url="https://t.me/tviyAstrogid_bot")]
])