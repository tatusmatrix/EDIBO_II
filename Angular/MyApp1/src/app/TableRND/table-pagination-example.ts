import {Component, OnInit, ViewChild} from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatTableDataSource} from '@angular/material/table';

import { SomeService, PeriodicElement } from './some.service';

/**
 * @title Angular + Material - How To Refresh A Data Source (mat-table)
 */
@Component({
  selector: 'table-pagination-example',
  styleUrls: ['table-pagination-example.css'],
  templateUrl: 'table-pagination-example.html',
})
export class TablePaginationExample implements OnInit {
  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  dataSource = new MatTableDataSource<PeriodicElement>([]);

  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;

  constructor(
    private myService: SomeService
  ) { }

  ngOnInit() {
    this.dataSource.paginator = this.paginator;
  }

  refresh() {
    this.myService.doSomething().subscribe((data: PeriodicElement[]) => {
      this.dataSource.data = data;
    });
  }
}



/**  Copyright 2019 Google Inc. All Rights Reserved.
    Use of this source code is governed by an MIT-style license that
    can be found in the LICENSE file at http://angular.io/license */