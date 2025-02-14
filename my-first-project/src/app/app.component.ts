import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MyCalcComponent } from './my-calc/my-calc.component';
import { bootstrapApplication } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MyCalcComponent, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  
}
