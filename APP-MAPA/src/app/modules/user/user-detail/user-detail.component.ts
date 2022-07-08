import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ICardUser } from '@shared/components/cards/card-user/icard-user.metadata';



@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html',
  styleUrls: ['./user-detail.component.scss']
})
export class UserDetailComponent implements OnInit {

  public id: number;
  public currentUser: ICardUser;
  constructor(
    private route: ActivatedRoute,

  ) {

  }

  ngOnInit() {
   
  }
}
