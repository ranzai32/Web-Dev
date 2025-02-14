import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-my-calc',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './my-calc.component.html',
  styleUrls: ['./my-calc.component.css']
})
export class MyCalcComponent {
  public first: number = 0;
  public second: number = 0;
  public operation: string = '+';
  public operations: string[] = ['+', '-', '*', '/'];
  public result?: number;

  public calc(): void {
    const num1 = Number(this.first);
    const num2 = Number(this.second);

    switch (this.operation) {
      case '+':
        this.result = num1 + num2;
        break;
      case '-':
        this.result = num1 - num2;
        break;
      case '*':
        this.result = num1 * num2;
        break;
      case '/':
        this.result = num2 !== 0 ? num1 / num2 : NaN; // Проверка на деление на 0
        break;
      default:
        this.result = NaN;
    }
  }
}
