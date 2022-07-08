import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserReservaComponent } from './user-reserva.component';

describe('UserReservaComponent', () => {
  let component: UserReservaComponent;
  let fixture: ComponentFixture<UserReservaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UserReservaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserReservaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
