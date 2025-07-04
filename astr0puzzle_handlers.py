from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from astr0puzzle_keyboard import (kwiz_question1, kwiz_question2, kwiz_question3, kwiz_question4, kwiz_question5,
                                  kwiz_question6, kwiz_question7, kwiz_question8, kwiz_question9, kwiz_question10, finall)
import requests

router = Router()

class Questions(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()
    question6 = State()
    question7 = State()
    question8 = State()
    question9 = State()
    question10 = State()
    final = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("1. Як часто ви схильні погоджуватися з думкою інших людей?", reply_markup=kwiz_question1)
    await state.set_state(Questions.question2)

@router.callback_query(Questions.question2)
async def cmd_question2(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("2. Як часто ти прикрашаєш правду? (Не хитруй, зізнавайся!)", reply_markup=kwiz_question2)
    await state.set_state(Questions.question3)

@router.callback_query(Questions.question3)
async def cmd_question3(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("3. Яка природна стихія вас найбільше приваблює?", reply_markup=kwiz_question3)
    await state.set_state(Questions.question4)

@router.callback_query(Questions.question4)
async def cmd_question4(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("4. Що з цього твоє?", reply_markup=kwiz_question4)
    await state.set_state(Questions.question5)

@router.callback_query(Questions.question5)
async def cmd_question5(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("5. Що в житті головне?", reply_markup=kwiz_question5)
    await state.set_state(Questions.question6)

@router.callback_query(Questions.question6)
async def cmd_question6(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("6. Який ти настрій у трьох словах?", reply_markup=kwiz_question6)
    await state.set_state(Questions.question7)

@router.callback_query(Questions.question7)
async def cmd_question7(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("7. Який колір тобі качає?", reply_markup=kwiz_question7)
    await state.set_state(Questions.question8)

@router.callback_query(Questions.question8)
async def cmd_question8(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("8. Як ти бачиш життя?", reply_markup=kwiz_question8)
    await state.set_state(Questions.question9)

@router.callback_query(Questions.question9)
async def cmd_question9(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("9. Що у світі важливіше за все?", reply_markup=kwiz_question9)
    await state.set_state(Questions.question10)

@router.callback_query(Questions.question10)
async def cmd_question10(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("10. Наскільки ти успішний?", reply_markup=kwiz_question10)
    await state.set_state(Questions.final)

@router.callback_query(Questions.final)
async def cmd_question11(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Чудово, щоб дізнатися відповідь перейдіть до вашого персонального астролога:", reply_markup=finall)




















