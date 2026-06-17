import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Conta } from '../conta/conta';

@Component({
  selector: 'app-welcome',
  imports: [ CommonModule, Conta],
  templateUrl: './welcome.html',
  styleUrl: './welcome.css',
})
export class Welcome {
  dataAtual = new Date();
}
