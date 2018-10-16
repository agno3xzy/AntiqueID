/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.controller;

import com.ejb.CommodityFacade;
import com.entity.Commodity;
import javax.inject.Named;
import javax.enterprise.context.SessionScoped;
import java.io.Serializable;
import javax.ejb.EJB;

/**
 *
 * @author agno3
 */
@Named(value = "auction")
@SessionScoped
public class auction implements Serializable {
@EJB 
private CommodityFacade commodityFacade1;
@EJB
private  CommodityFacade commodityFacade;
    /**
     * Creates a new instance of NewJSFManagedBean
     */
    public auction() {
        
    }

  
    public String Search(){
        return commodityFacade.Search().get(0).toString();
    }
    public void try1(int newstartprice,int id){
        Commodity entity =commodityFacade1.find(id);
        entity.setCommStartprice(newstartprice);
        commodityFacade.edit(entity);
    }
}
