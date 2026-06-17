import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Welcome } from './welcome/welcome';

@Component({
  selector: 'app-banner',
  standalone: true,
  imports: [CommonModule, Welcome], 
  templateUrl: './banner.html',
  styleUrls: ['./banner.css'] 
})
export class BannerComponent {
  dataAtual = new Date();
}