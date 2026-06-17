import { CommonModule } from '@angular/common';
import { Component, signal } from '@angular/core';
import { BannerComponent } from './banner/banner';

@Component({
  selector: 'app-root',
  imports: [CommonModule, BannerComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('biabank');
}
