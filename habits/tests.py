from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import CustomUser


class HabitAPITest(APITestCase):
    """ Тестирование работы с привычками """

    def setUp(self):
        """ Инициализация пользователя и привычки для тестов """

        self.user = CustomUser.objects.create(
            email="user@example.com",
            password="securepassword"
        )
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place="Офис",
            time="09:00:00",
            action="Начать рабочий день",
            duration=30,
            is_daily=True,
        )

    def test_create_new_habit(self):
        """ Тест создания новой привычки """

        url = reverse("habits:create_habit")
        payload = {
            "owner": self.user.pk,
            "place": "Кафе",
            "time": "12:00:00",
            "action": "Обеденный перерыв",
            "duration": 45,
            "is_daily": True,
        }

        response = self.client.post(url, data=payload)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data.get("owner"), self.user.pk)
        self.assertEqual(response_data.get("place"), "Кафе")
        self.assertEqual(response_data.get("time"), "12:00:00")
        self.assertEqual(response_data.get("action"), "Обеденный перерыв")
        self.assertEqual(response_data.get("duration"), 45)
        self.assertEqual(response_data.get("is_daily"), True)

    def test_get_habit_list(self):
        """ Тест получения списка всех привычек пользователя """

        response = self.client.get(reverse('habits:list_habits'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_single_habit(self):
        """ Тест детального просмотра одной привычки """

        url = reverse("habits:view_habit", args=(self.hhabit.pk,))
        response = self.client.get(url)
        habit_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(habit_data.get("owner"), self.hhabit.owner.id)
        self.assertEqual(habit_data.get("place"), self.hhabit.place)
        self.assertEqual(habit_data.get("time"), self.hhabit.time)
        self.assertEqual(habit_data.get("action"), self.hhabit.action)
        self.assertEqual(habit_data.get("duration"), self.hhabit.duration)
        self.assertEqual(habit_data.get("is_daily"), self.hhabit.is_daily)

    def test_modify_habit(self):
        """ Тест обновления привычки """

        url = reverse("habits:update_habit", args=(self.hhabit.pk,))
        update_data = {
            "owner": self.user.pk,
            "place": "Спортзал",
            "time": "07:30:00",
            "action": "Тренировка",
            "duration": 90,
            "is_daily": True,
        }
        response = self.client.put(url, update_data)
        updated_habit = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_habit.get("owner"), self.hhabit.owner.id)
        self.assertEqual(updated_habit.get("place"), "Спортзал")
        self.assertEqual(updated_habit.get("time"), "07:30:00")
        self.assertEqual(updated_habit.get("action"), "Тренировка")
        self.assertEqual(updated_habit.get("duration"), 90)
        self.assertEqual(updated_habit.get("is_daily"), True)

    def test_remove_habit(self):
        """ Тест удаления привычки """

        url = reverse("habits:delete_habit", args=(self.hhabit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_public_habits(self):
        """ Тест получения публичных привычек """

        response = self.client.get(reverse('habits:list_public_habits'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)