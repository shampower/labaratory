from appJar import gui
import random
from enum import Enum

# Собственные исключения
class SnakeGameException(Exception):
    """Базовое исключение для игры Змейка"""
    pass

class CollisionException(SnakeGameException):
    """Исключение при столкновении"""
    pass

class InvalidDirectionException(SnakeGameException):
    """Исключение при недопустимом направлении"""
    pass

class Direction(Enum):
    """Перечисление возможных направлений движения змейки"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Snake:
    """Класс, представляющий змейку"""
    def __init__(self, canvas_size, cell_size):
        self.cell_size = cell_size
        self.canvas_size = canvas_size
        self.reset()
        
    def reset(self):
        """Сброс змейки в начальное состояние"""
        start_x = self.canvas_size // 2
        start_y = self.canvas_size // 2
        self.body = [(start_x, start_y), 
                    (start_x - 1, start_y), 
                    (start_x - 2, start_y)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.grow = False
        
    def change_direction(self, new_direction):
        """Изменение направления движения змейки"""
        # Запрещаем разворот на 180 градусов
        if (new_direction.value - self.direction.value) % 4 != 2:
            self.next_direction = new_direction
    
    def move(self):
        """Движение змейки"""
        self.direction = self.next_direction
        
        # Получаем координаты головы
        head_x, head_y = self.body[0]
        
        # Вычисляем новое положение головы в зависимости от направления
        if self.direction == Direction.UP:
            new_head = (head_x, head_y - 1)
        elif self.direction == Direction.RIGHT:
            new_head = (head_x + 1, head_y)
        elif self.direction == Direction.DOWN:
            new_head = (head_x, head_y + 1)
        elif self.direction == Direction.LEFT:
            new_head = (head_x - 1, head_y)
        else:
            raise InvalidDirectionException("Недопустимое направление движения")
        
        # Проверяем столкновение с границами поля
        if (new_head[0] < 0 or new_head[0] >= self.canvas_size or 
            new_head[1] < 0 or new_head[1] >= self.canvas_size):
            raise CollisionException("Столкновение с границей поля")
            
        # Проверяем столкновение с телом
        if new_head in self.body[:-1]:
            raise CollisionException("Столкновение с телом змейки")
            
        # Добавляем новую голову
        self.body.insert(0, new_head)
        
        # Если змейка не должна расти, удаляем хвост
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def check_food_collision(self, food):
        """Проверяем, съела ли змейка еду"""
        if self.body[0] == food:
            self.grow = True
            return True
        return False
    
    def draw(self, app):
        """Отрисовка змейки"""
        for segment in self.body:
            x, y = segment
            app.addCanvasRectangle("game", 
                                 x * self.cell_size, 
                                 y * self.cell_size, 
                                 self.cell_size, 
                                 self.cell_size, 
                                 fill="green")

class Food:
    """Класс, представляющий еду для змейки"""
    def __init__(self, canvas_size, cell_size):
        self.cell_size = cell_size
        self.canvas_size = canvas_size
        self.position = (0, 0)
        self.spawn()
        
    def spawn(self, snake_body=None):
        """Появление еды в случайном месте"""
        if snake_body is None:
            snake_body = []
            
        # Генерируем случайные позиции, пока не найдем свободную
        while True:
            x = random.randint(0, self.canvas_size - 1)
            y = random.randint(0, self.canvas_size - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break
    
    def draw(self, app):
        """Отрисовка еды"""
        x, y = self.position
        app.addCanvasRectangle("game", 
                             x * self.cell_size, 
                             y * self.cell_size, 
                             self.cell_size, 
                             self.cell_size, 
                             fill="red")

class SnakeGame:
    """Основной класс игры"""
    def __init__(self, app, canvas_size=20, cell_size=20):
        self.app = app
        self.canvas_size = canvas_size
        self.cell_size = cell_size
        self.snake = Snake(canvas_size, cell_size)
        self.food = Food(canvas_size, cell_size)
        self.score = 0
        self.game_over = False
        self.speed = 200  # начальная скорость (меньше = быстрее)
        
        # Настройка интерфейса
        self.setup_gui()
        
    def setup_gui(self):
        """Настройка графического интерфейса"""
        self.app.setTitle("Змейка")
        self.app.setSize(self.canvas_size * self.cell_size + 20, 
                        self.canvas_size * self.cell_size + 70)
        self.app.setFont(12)
        
        # Создаем холст для игры
        self.app.addLabel("score", f"Счет: {self.score}", 0, 0)
        self.app.addCanvas("game", 1, 0, 
                         self.canvas_size * self.cell_size, 
                         self.canvas_size * self.cell_size)
        self.app.addButton("Новая игра", self.reset_game, 2, 0)
        
        # Привязываем клавиши управления
        self.app.bindKey("<Up>", lambda _: self.snake.change_direction(Direction.UP))
        self.app.bindKey("<Right>", lambda _: self.snake.change_direction(Direction.RIGHT))
        self.app.bindKey("<Down>", lambda _: self.snake.change_direction(Direction.DOWN))
        self.app.bindKey("<Left>", lambda _: self.snake.change_direction(Direction.LEFT))
        
        # Запускаем игровой цикл
        self.update()
    
    def update(self):
        """Обновление игрового состояния"""
        if not self.game_over:
            try:
                # Двигаем змейку
                self.snake.move()
                
                # Проверяем, съела ли змейка еду
                if self.snake.check_food_collision(self.food.position):
                    self.score += 10
                    self.app.setLabel("score", f"Счет: {self.score}")
                    self.food.spawn(self.snake.body)
                    
                    # Увеличиваем скорость каждые 50 очков
                    if self.score % 50 == 0 and self.speed > 50:
                        self.speed -= 10
                
                # Очищаем холст и перерисовываем игру
                self.app.clearCanvas("game")
                self.snake.draw(self.app)
                self.food.draw(self.app)
                
            except CollisionException:
                self.game_over = True
                self.app.infoBox("Конец игры", f"Игра окончена! Ваш счет: {self.score}")
        
        # Планируем следующее обновление
        self.app.after(self.speed, self.update)
    
    def reset_game(self):
        """Сброс игры"""
        self.snake.reset()
        self.food.spawn(self.snake.body)
        self.score = 0
        self.game_over = False
        self.speed = 200
        self.app.setLabel("score", f"Счет: {self.score}")
        self.app.clearCanvas("game")
        self.snake.draw(self.app)
        self.food.draw(self.app)

# Создаем и запускаем приложение
app = gui()
game = SnakeGame(app)
app.go()