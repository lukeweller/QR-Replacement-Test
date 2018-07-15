//
//  SecondViewController.swift
//  QR-Replacement-Test
//
//  Created by Luke Weller on 7/1/18.
//  Copyright © 2018 Luke Weller. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {

    @IBOutlet weak var testPhotoFull: UIImageView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.testPhotoFull.image = UIImage(named: "insta0")
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

